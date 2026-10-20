from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import self_energy_discard_attack, condition_attack


card = PokemonCardDef(
    guid="91aa03bb-8425-55aa-9941-65d3f0a106b0",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1", "Volcarona"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE, PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Attack(
            title="Shimmering Scales",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused. If tails, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True, tails_conditions=(SpecialConditions.PARALYZED,)),
        ),
        Attack(
            title="Power Hurricane",
            game_text="Discard all Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)