from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.passives_common import ability_lock_passive, opposing_pokemon


def _rapid_strike_lock(pokemon, carrier):
    return opposing_pokemon(pokemon, carrier) and "Rapid Strike" in subtypes_for(pokemon.archetype_id)

card = PokemonCardDef(
    guid="2f698a4c-92c4-55f9-a0b5-99cb79912b5c",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gorebyss.Name",
    display_name="Gorebyss",
    searchable_by=["Gorebyss", "Stage 1", "Fusion Strike", "Gorebyss"],
    subtypes=["Stage 1", "Fusion Strike"],
    collector_number=67,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Ability(
            title="Rapid Strike Canceler",
            game_text="Your opponent's Rapid Strike Pok\u00e9mon in play have no Abilities.",
            passive=ability_lock_passive(_rapid_strike_lock),
        ),
        Attack(
            title="Draining Kiss",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=heal_attack(30, target="self"),
        ),
    ],
)