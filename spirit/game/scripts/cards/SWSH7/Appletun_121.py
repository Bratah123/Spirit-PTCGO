from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, defender_is_v
from spirit.game.session.effects import is_special_energy


async def thick_mucus(ctx):
    """70 for each Special Energy card attached to the opponent's Pokemon."""
    count = sum(
        1 for p in ctx.opponent_pokemon_in_play()
        for e in ctx.attached_energies(p) if is_special_energy(e)
    )
    await ctx.deal_damage(70 * count)

card = PokemonCardDef(
    guid="ade82de6-2bc0-5531-bc7a-3ebc2dbd264c",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Appletun.Name",
    display_name="Appletun",
    searchable_by=["Appletun", "Stage 1", "Appletun"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Thick Mucus",
            game_text="This attack does 70 damage for each Special Energy card attached to your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=thick_mucus,
        ),
        Attack(
            title="Fighting Tackle",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(defender_is_v, 80),
        ),
    ],
)