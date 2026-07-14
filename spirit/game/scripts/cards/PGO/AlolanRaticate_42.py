from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def super_fang(ctx):
    """Damage counters on the opponent's Active until its remaining HP is 10."""
    target = ctx.defender
    if target is None:
        return
    hp = target.get_attribute(AttrID.HP, 0)
    if hp > 10:
        await ctx.deal_damage(hp - 10, target=target, as_counters=True)


card = PokemonCardDef(
    guid="2d7be742-d405-5c3c-befb-5ef93a4db3ea",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRaticate.Name",
    display_name="Alolan Raticate",
    searchable_by=["Alolan Raticate", "Stage 1", "AlolanRaticate"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="PGO",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Chase Up",
            game_text="Search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=search_to_hand(
                None, count=1, reveal=False,
                prompt="Choose a card to put into your hand.",
            ),
        ),
        Attack(
            title="Super Fang",
            game_text="Put damage counters on your opponent's Active Pokémon until its remaining HP is 10.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=super_fang,
        ),
    ],
)
