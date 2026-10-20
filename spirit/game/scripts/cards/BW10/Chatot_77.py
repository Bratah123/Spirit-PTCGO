from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="89af03ee-1374-5f3d-9f1a-fb147a7bea92",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chatot.Name",
    display_name="Chatot",
    searchable_by=["Chatot", "Basic", "Team Plasma", "Chatot"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=77,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=441,
    abilities=[
        Attack(
            title="Misinformation",
            game_text="Discard all Pok\u00e9mon Tool cards attached to each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Tone-Deaf",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)