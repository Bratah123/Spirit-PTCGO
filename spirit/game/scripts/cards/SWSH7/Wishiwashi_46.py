from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.passives import Passive


class GroupPowerPassive(Passive):
    """This Pokemon gets +150 HP if it has 3 or more Water Energy attached."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier:
            return 0
        count = sum(1 for c in carrier.children
                    if energy_provides_type(c, PokemonTypes.WATER.value))
        return 150 if count >= 3 else 0


def _basic_energy_count_self(ctx):
    return sum(1 for e in ctx.attached_energies(ctx.attacker) if is_basic_energy_card(e))

card = PokemonCardDef(
    guid="1bb51612-663b-5e74-abc5-2e1d4005b13d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name",
    display_name="Wishiwashi",
    searchable_by=["Wishiwashi", "Basic", "Rapid Strike", "Wishiwashi"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=46,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Ability(
            title="Group Power",
            game_text="If this Pok\u00e9mon has 3 or more Water Energy attached, it gets +150 HP.",
            passive=GroupPowerPassive(),
        ),
        Attack(
            title="Schooling Shot",
            game_text="This attack does 30 more damage for each basic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(_basic_energy_count_self, 30, base=30),
        ),
    ],
)