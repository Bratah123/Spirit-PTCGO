from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.session.passives import Passive


class MetalShieldPassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.target is carrier):
            return
        if any(is_energy_card(c) for c in carrier.children):
            calc.amount = max(0, calc.amount - 30)


def _kos_suffered_last_turn(ctx):
    return ctx.kos_suffered_last_turn() > 0


card = PokemonCardDef(
    guid="c7a2fabe-fc1b-5678-bbf6-dc7149451a87",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zamazenta.Name",
    display_name="Zamazenta",
    searchable_by=["Zamazenta", "Basic", "Zamazenta"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=889,
    abilities=[
        Ability(
            title="Metal Shield",
            game_text="If this Pok\u00e9mon has any Energy attached, it takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=MetalShieldPassive(),
        ),
        Attack(
            title="Retaliate",
            game_text="If any of your Pok\u00e9mon were Knocked Out during your opponent's last turn, this attack does 120 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=bonus_if(_kos_suffered_last_turn, 120),
        ),
    ],
)