from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm3 import bye_bye_heal


card = PokemonCardDef(
    guid="400314cf-bcf5-532b-b723-2bae6a488e12",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2", "Butterfree"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Bye-Bye Heal",
            game_text="Heal all damage from all of your Pok\u00e9mon. Shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=bye_bye_heal,
        ),
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
