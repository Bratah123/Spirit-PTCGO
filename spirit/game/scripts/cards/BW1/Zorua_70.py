from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="17b42c1d-a531-5be7-ae88-761794f7eff1",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    display_name="Zorua",
    searchable_by=["Zorua", "Basic", "Zorua"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=570,
    abilities=[
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)