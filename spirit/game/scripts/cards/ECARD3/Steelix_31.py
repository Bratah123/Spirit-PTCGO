from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import RareMetalPassive, metal_tail


card = PokemonCardDef(
    guid="5c53fb3e-a892-5acd-b349-6a92ebc52963",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1", "Steelix"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=208,
    abilities=[
        Ability(
            title="Rare Metal",
            game_text="All basic Energy cards attached to Steelix provide Metal Energy instead of their usual types.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=RareMetalPassive(),
        ),
        Attack(
            title="Squeeze",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage and the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=condition_attack(
                SpecialConditions.PARALYZED, flip=True, heads_bonus_damage=10),
        ),
        Attack(
            title="Metal Tail",
            game_text="Before doing damage, you may flip a coin. If heads, this attack does 80 damage. If tails, this attack does nothing.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=metal_tail,
        ),
    ],
)
