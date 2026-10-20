from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.session.passives import Passive, carrier_pokemon


class _DespoticFang(Passive):
    """Damage from this Pokemon's attacks ignores effects on the opponent's Active."""
    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is not None and calc.attacker is me and calc.is_attack and calc.is_opposing and calc.to_active:
            calc.ignore_target_effects = True


card = PokemonCardDef(
    guid="4878d363-3f3e-52f4-a3c7-ba3c810437fb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TyrantrumEX.Name",
    display_name="Tyrantrum-EX",
    searchable_by=["Tyrantrum-EX", "Basic", "EX", "TyrantrumEX"],
    subtypes=["Basic", "EX"],
    collector_number=70,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=697,
    abilities=[
        Ability(
            title="Despotic Fang",
            game_text="Damage from this Pok\u00e9mon's attacks isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            passive=_DespoticFang(),
        ),
        Attack(
            title="Dragon Fang",
            game_text="Discard 3 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)