from spirit.game.card_effects.attacks_common import damage_per, count_in_play
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.pokemon import is_pokemon_gx
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _is_v_or_gx(pokemon):
    return is_pokemon_v(pokemon.archetype_id) or is_pokemon_gx(pokemon.archetype_id)

card = PokemonCardDef(
    guid="14780490-9698-5d31-9e28-977068e717df",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golisopod.Name",
    display_name="Golisopod",
    searchable_by=["Golisopod", "Stage 1", "Golisopod"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Attack(
            title="Hard Times Slash",
            game_text="This attack does 50 more damage for each of your opponent's Pok\u00e9mon V and Pok\u00e9mon-GX in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_in_play("opponent", _is_v_or_gx), 50, base=30),
        ),
        Attack(
            title="Smash Turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=switch_self_attack(),
        ),
    ],
)