from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.ex import defender_is_ex


async def super_slap_push(ctx):
    """Does 20 damage to each Defending Pok\u00e9mon (no printed damage)."""
    await ctx.deal_damage(20)


card = PokemonCardDef(
    guid="6b8940a4-b5e4-558d-b0d6-f8ce9a9ed8ec",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name",
    display_name="Hariyama",
    searchable_by=["Hariyama", "Stage 1", "Hariyama"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Attack(
            title="Super Slap Push",
            game_text="Does 20 damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=0,
            effect=super_slap_push,
        ),
        Attack(
            title="Mega Throw",
            game_text="If the Defending Pok\u00e9mon is a Pok\u00e9mon-ex, this attack does 40 damage plus 40 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bonus_if(defender_is_ex, 40),
        ),
    ],
)
