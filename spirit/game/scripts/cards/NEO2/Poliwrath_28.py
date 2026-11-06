from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="73f591e4-76e4-5a44-af36-ac941696c155",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2", "Poliwrath"],
    subtypes=["Stage 2"],
    collector_number=28,
    set_code="NEO2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Submission",
            game_text="Poliwrath does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=recoil_attack(20),
        ),
    ],
)
