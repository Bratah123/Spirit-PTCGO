from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1ed74e86-4962-548b-8910-d8fb0d187d5f",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corviknight.Name",
    display_name="Corviknight",
    searchable_by=["Corviknight", "Stage 2", "Corviknight"],
    subtypes=["Stage 2"],
    collector_number=190,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corvisquire.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Power Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=unimplemented,
        ),
    ],
)