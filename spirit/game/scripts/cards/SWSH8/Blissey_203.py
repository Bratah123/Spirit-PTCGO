from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_bench, has_attack_titled
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.pokemon import is_pokemon_vmax

_has_rollout = has_attack_titled("Let's All Rollout")


def _expert_in_roundness_pred(calc, carrier):
    return (
        calc.target.owning_player_id == carrier.owning_player_id
        and _has_rollout(calc.target)
        and is_pokemon_vmax(calc.attacker.archetype_id)
    )


card = PokemonCardDef(
    guid="d4a569ea-e41b-5229-8588-ae1f7ffd1c17",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=203,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Expert in Roundness",
            game_text="Prevent all damage done to each of your Pokémon that has the Let's All Rollout attack by attacks from your opponent's Pokémon VMAX.",
            passive=prevent_damage_when(_expert_in_roundness_pred),
        ),
        Attack(
            title="Let's All Rollout",
            game_text="This attack does 20 damage for each of your Benched Pokémon that has the Let's All Rollout attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_bench("mine", pred=_has_rollout), 20),
        ),
    ],
)
