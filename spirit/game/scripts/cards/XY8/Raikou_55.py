from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.attacks_common import damage_per, count_energy


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


class _ShiningBody(Passive):
    """With any Lightning Energy attached, damage from attacks to this Pokemon is reduced by 20."""
    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.target is me and me is not None):
            return
        if any(is_energy_card(c) and _is_lightning_energy(c) for c in me.children):
            calc.amount = max(0, calc.amount - 20)


card = PokemonCardDef(
    guid="a630362e-3388-54d6-8cb7-0b671f8ad161",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=243,
    abilities=[
        Ability(
            title="Shining Body",
            game_text="If this Pok\u00e9mon has any Lightning Energy attached to it, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            passive=_ShiningBody(),
        ),
        Attack(
            title="Thunder Lance",
            game_text="This attack does 20 more damage for each Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.LIGHTNING), 20, base=50),
        ),
    ],
)