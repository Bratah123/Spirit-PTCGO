from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, ignore_resistance_attack


card = PokemonCardDef(
    guid="72484f6d-1a27-58a9-9408-2a9524013b61",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name",
    display_name="Breloom",
    searchable_by=["Breloom", "Stage 1", "Breloom"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    family_id=285,
    abilities=[
        Attack(
            title="Super Poison Breath",
            game_text="Each Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Sky Uppercut",
            game_text="This attack's damage is not affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ignore_resistance_attack(),
        ),
    ],
)
