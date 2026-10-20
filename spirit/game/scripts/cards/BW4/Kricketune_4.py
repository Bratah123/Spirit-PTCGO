from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="d649b036-77f2-566e-8dc4-8e6ff4a92ce0",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketune.Name",
    display_name="Kricketune",
    searchable_by=["Kricketune", "Stage 1", "Kricketune"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name",
    family_id=401,
    abilities=[
        Attack(
            title="White Noise",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Draining Cut",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads. Heal from this Pok\u00e9mon the same amount of damage you did to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)