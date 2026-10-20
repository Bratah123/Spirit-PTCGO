from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f4306236-3046-5709-bf22-baba5a76d239",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    display_name="Trubbish",
    searchable_by=["Trubbish", "Basic", "Trubbish"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=568,
    abilities=[
        Attack(
            title="Tool Drop",
            game_text="Does 20 damage for each Pok\u00e9mon Tool card attached to Pok\u00e9mon in play (both yours and your opponent's).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)