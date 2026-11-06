from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_in_play, damage_counters_on


def _is_darkness_pokemon(pokemon):
    return PokemonTypes.DARKNESS.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="cf4fe2e9-e1bf-5880-bcfb-bb2336527157",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1", "Zoroark"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Brutal Bash",
            game_text="Does 20 damage times the number of Darkness Pok\u00e9mon you have in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_in_play('mine', _is_darkness_pokemon), 20),
        ),
        Attack(
            title="Dark Rush",
            game_text="Does 20 damage times the number of damage counters on this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(damage_counters_on('self'), 20),
        ),
    ],
)