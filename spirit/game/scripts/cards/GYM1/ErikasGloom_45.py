from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import flip_heal_self, magic_pollen


card = PokemonCardDef(
    guid="74b841bd-99ab-5705-853c-3c1df075f4e8",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasGloom.Name",
    display_name="Erika's Gloom",
    searchable_by=["Erika's Gloom", "Stage 1", "ErikasGloom"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasOddish.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Healing Pollen",
            game_text="Flip a coin. If heads, remove 4 damage counters from Erika's Gloom. If Erika's Gloom has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 1},
            effect=flip_heal_self,
        ),
        Attack(
            title="Magic Pollen",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep, Confused, Paralyzed, or Poisoned (your choice).",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            effect=magic_pollen,
        ),
    ],
)
