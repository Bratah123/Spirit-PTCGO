from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import wild_growth


card = PokemonCardDef(
    guid="9d384009-c959-551a-96f8-8a14c3478556",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium",
    searchable_by=["Meganium", "Stage 2", "Meganium"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=152,
    abilities=[
        Ability(
            title="Wild Growth",
            game_text="As long as Meganium is in play each Grass Energy card attached to your Grass Pok\u00e9mon instead provides GrassGrass. This power stops working while Meganium is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=wild_growth,
        ),
        Attack(
            title="Soothing Scent",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 4},
            damage=40,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
