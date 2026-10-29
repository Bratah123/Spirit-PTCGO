from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import AttrID
from spirit.game.card_effects.passives_common import prevent_damage_when

def _heatproof_pred(calc, carrier):
    if calc.target is not carrier:
        return False
    types = calc.attacker.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIRE.value in types

card = PokemonCardDef(
    guid="f5cd6102-f5ff-5f45-aca0-5463ac76eb4f",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Araquanid.Name",
    display_name="Araquanid",
    searchable_by=["Araquanid", "Stage 1", "Araquanid"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name",
    family_id=751,
    abilities=[
        Ability(
            title="Water Bubble",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Fire Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            passive=prevent_damage_when(_heatproof_pred),
        ),
        Attack(
            title="Aqua Edge",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)