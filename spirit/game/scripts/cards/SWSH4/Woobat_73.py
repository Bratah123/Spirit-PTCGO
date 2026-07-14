from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents


async def unamplified_soundwave(ctx):
    """30 to each of your opponent's Pokemon (no W/R on the Bench). Does
    nothing if you have any cards in your hand."""
    if ctx.hand_size():
        return
    await damage_all_opponents(30)(ctx)


card = PokemonCardDef(
    guid="21552761-0ded-5e64-989a-9e6871c81489",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    display_name="Woobat",
    searchable_by=["Woobat", "Basic", "Woobat"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=527,
    abilities=[
        Attack(
            title="Unamplified Soundwave",
            game_text="This attack does 30 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) If you have any cards in your hand, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unamplified_soundwave,
        ),
    ],
)
