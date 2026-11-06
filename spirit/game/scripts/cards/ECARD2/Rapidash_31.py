from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection
from spirit.game.card_effects.ecard import gallop


card = PokemonCardDef(
    guid="ddf9eebe-4abd-5e5d-aea6-60d2aa2cb648",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name",
    display_name="Rapidash",
    searchable_by=["Rapidash", "Stage 1", "Rapidash"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    family_id=77,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Rapidash.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Gallop",
            game_text="Flip a coin. If heads, discard a Fire Energy card attached to Rapidash and this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=gallop,
        ),
    ],
)
