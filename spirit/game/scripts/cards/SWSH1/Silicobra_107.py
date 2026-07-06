from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5587f71b-a34a-529d-a92e-370ec6e0973e",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name",
    display_name="Silicobra",
    searchable_by=["Silicobra", "Basic", "Silicobra"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=843,
    abilities=[
        Attack(
            title="Sand Attack",
            game_text="During your opponent's next turn, if the Defending Pok\u00e9mon tries to attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)