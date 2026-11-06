from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_bonus_attack
from spirit.game.card_effects.ecard import miracle_tail


card = PokemonCardDef(
    guid="fa3b1ed6-cfb9-5923-b87e-14848cf3f2c1",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Miracle Tail",
            game_text="Flip a coin. If heads, choose a Special Condition (Asleep, Burned, Confused, Paralyzed, or Poisoned). The Defending Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=miracle_tail,
        ),
        Attack(
            title="Roasting Heat",
            game_text="If the Defending Pok\u00e9mon is Burned, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=condition_bonus_attack(20, SpecialConditions.BURNED),
        ),
    ],
)
