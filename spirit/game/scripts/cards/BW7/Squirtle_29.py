from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.passives_common import is_in_active_spot


class _ShellShieldPassive(Passive):
    """While this Pokemon is on your Bench, prevent all damage done to it by
    attacks (both yours and your opponent's)."""

    def prevents_damage(self, calc, carrier):
        target = carrier_pokemon(carrier)
        return bool(calc.is_attack and target is calc.target and not is_in_active_spot(target))


card = PokemonCardDef(
    guid="6d9a9ccf-b043-56d2-86d3-8dff78e6c9cb",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    display_name="Squirtle",
    searchable_by=["Squirtle", "Basic", "Squirtle"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=7,
    abilities=[
        Ability(
            title="Shell Shield",
            game_text="As along as this Pok\u00e9mon is on your Bench, prevent all damage done to this Pok\u00e9mon by attacks (both yours and your opponent's).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_ShellShieldPassive(),
        ),
        Attack(
            title="Water Splash",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)