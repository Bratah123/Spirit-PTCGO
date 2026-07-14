from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when


def _heatproof_pred(calc, carrier):
    if calc.target is not carrier:
        return False
    types = calc.attacker.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIRE.value in types


card = PokemonCardDef(
    guid="79c18e5d-69ef-53e6-a6aa-91bbbc1d5153",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=112,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Ability(
            title="Heatproof",
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Fire Pokémon.",
            passive=prevent_damage_when(_heatproof_pred),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
