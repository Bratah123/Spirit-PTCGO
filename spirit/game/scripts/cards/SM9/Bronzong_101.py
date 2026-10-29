from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import AttrID, SpecialConditions
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.attacks_common import condition_attack

def _heatproof_pred(calc, carrier):
    if calc.target is not carrier:
        return False
    types = calc.attacker.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIRE.value in types

card = PokemonCardDef(
    guid="d98d6d80-dcc4-523f-b673-17385ca0c634",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=101,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Ability(
            title="Heatproof",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Fire Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=prevent_damage_when(_heatproof_pred),
        ),
        Attack(
            title="Shady Stamp",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)