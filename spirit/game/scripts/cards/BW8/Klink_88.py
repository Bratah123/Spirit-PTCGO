from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="212c3ae1-c5eb-5a73-915c-b1477b47a29b",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    display_name="Klink",
    searchable_by=["Klink", "Basic", "Klink"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=599,
    abilities=[
        Attack(
            title="Rigidify",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Vice Grip",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)