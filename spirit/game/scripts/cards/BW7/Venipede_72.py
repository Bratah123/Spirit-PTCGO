from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="9e906f62-7af8-5024-b2f0-153b9bf09daf",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name",
    display_name="Venipede",
    searchable_by=["Venipede", "Basic", "Venipede"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=543,
    abilities=[
        Ability(
            title="Poison Point",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Poisoned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)