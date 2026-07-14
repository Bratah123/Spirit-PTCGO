from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.passives_common import prevent_damage_when


def _metal_lodging_pred(calc, carrier):
    target = calc.target
    if target is None or target.owning_player_id != carrier.owning_player_id:
        return False
    if not is_basic_pokemon(target):
        return False
    if not any(energy_provides_type(e, PokemonTypes.METAL.value) for e in target.children):
        return False
    attacker = calc.attacker
    return attacker is not None and is_pokemon_v(attacker.archetype_id)


card = PokemonCardDef(
    guid="a04130db-d9da-503c-af2c-e4ea5789030f",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGoodra.Name",
    display_name="Hisuian Goodra",
    searchable_by=["Hisuian Goodra", "Stage 2", "HisuianGoodra"],
    subtypes=["Stage 2"],
    collector_number=134,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSliggoo.Name",
    family_id=704,
    abilities=[
        Ability(
            title="Metal Lodging",
            game_text="Prevent all damage done to each of your Basic Pok\u00e9mon that has any Metal Energy attached by attacks from your opponent's Pok\u00e9mon V.",
            passive=prevent_damage_when(_metal_lodging_pred),
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)