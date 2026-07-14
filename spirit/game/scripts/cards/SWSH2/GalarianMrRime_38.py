from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.passives_common import attack_effect_shield_passive
from spirit.game.card_effects.pokemon import is_energy_card


def _has_energy_attached(pokemon) -> bool:
    return any(is_energy_card(c) for c in getattr(pokemon, "children", []))


def _screen_cleaner_protects(target, carrier) -> bool:
    return target.owning_player_id == carrier.owning_player_id \
        and _has_energy_attached(target)


card = PokemonCardDef(
    guid="8fb41ba0-f1ad-54ae-b56c-91d0ef89c4e5",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrRime.Name",
    display_name="Galarian Mr. Rime",
    searchable_by=["Galarian Mr. Rime", "Stage 1", "GalarianMrRime"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrMime.Name",
    family_id=122,
    abilities=[
        Ability(
            title="Screen Cleaner",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to all of your Pokémon that have Energy attached. (Existing effects are not removed.)",
            passive=attack_effect_shield_passive(protects=_screen_cleaner_protects),
        ),
        Attack(
            title="Triple Spin",
            game_text="Flip 3 coins. This attack does 50 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=50),
        ),
    ],
)
