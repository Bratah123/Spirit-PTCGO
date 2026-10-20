from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.session.passives import Passive, carrier_pokemon


def _has_fighting_resistance(ctx) -> bool:
    defender = ctx.defender
    return defender is not None and \
        defender.get_attribute(AttrID.RESISTANCE_TYPES) == PokemonTypes.FIGHTING.value


class _ZapZone(Passive):
    """Damage from your Lightning Pokemon's attacks isn't affected by effects on the opponent's Active."""
    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        att = calc.attacker
        if (me is not None and att is not None and calc.is_attack and calc.is_opposing and calc.to_active
                and att.owning_player_id == me.owning_player_id
                and PokemonTypes.LIGHTNING.value in (att.get_attribute(AttrID.POKEMON_TYPES) or [])):
            calc.ignore_target_effects = True


card = PokemonCardDef(
    guid="18d45e1c-a8b1-5888-8a77-8c96b75405b3",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name",
    display_name="Zebstrika",
    searchable_by=["Zebstrika", "Stage 1", "Zebstrika"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    family_id=522,
    abilities=[
        Ability(
            title="Zap Zone",
            game_text="Damage from the attacks of your Lightning Pok\u00e9mon isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            passive=_ZapZone(),
        ),
        Attack(
            title="Crashing Bolt",
            game_text="If your opponent's Active Pok\u00e9mon has Fighting Resistance, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_has_fighting_resistance, 60),
        ),
    ],
)