from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import AttrID, PokemonTypes


from spirit.game.card_effects.passives_common import team_damage_boost_passive


def _is_metal_pokemon(pokemon):
    return PokemonTypes.METAL.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="815ec207-db88-5df7-adce-f30c560cb718",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name",
    display_name="Dhelmise",
    searchable_by=["Dhelmise", "Basic", "Dhelmise"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=781,
    abilities=[
        Ability(
            title="Steelworker",
            game_text="Your Metal Pok\u00e9mon's attacks do 10 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=team_damage_boost_passive(10, attacker_pred=_is_metal_pokemon),
            effect=None,
        ),
        Attack(
            title="Anchor Shot",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)