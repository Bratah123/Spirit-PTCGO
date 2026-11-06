from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import final_beam


card = PokemonCardDef(
    guid="bd21e118-9e3b-5bf4-bbb8-4ec1a921c0e8",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGyarados.Name",
    display_name="Dark Gyarados",
    searchable_by=["Dark Gyarados", "Stage 1", "DarkGyarados"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Ability(
            title="Final Beam",
            game_text="When Dark Gyarados is Knocked Out by an attack, flip a coin. If heads, this power does 20 damage for each Water Energy attached to Dark Gyarados to the Pok\u00e9mon that Knocked Out Dark Gyarados. Apply Weakness and Resistance. This power doesn't work if Dark Gyarados is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=final_beam,
        ),
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 3},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
