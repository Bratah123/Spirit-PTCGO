from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack, mill_attack


card = PokemonCardDef(
    guid="3d88d26b-7ad1-5feb-b69a-89f0ab4958e6",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name",
    display_name="Garchomp",
    searchable_by=["Garchomp", "Stage 2", "Garchomp"],
    subtypes=["Stage 2"],
    collector_number=90,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Mach Cut",
            game_text="Discard a Special Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
        Attack(
            title="Dragonblade",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=100,
            effect=mill_attack(2, opponent=False),
        ),
    ],
)