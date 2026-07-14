from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a73a724a-b032-5440-920c-01bd5c74f571",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardVMAX.Name",
    display_name="Charizard VMAX",
    searchable_by=["Charizard VMAX", "VMAX", "CharizardVMAX"],
    subtypes=["VMAX"],
    collector_number=20,
    set_code="SWSH3",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardV.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
        Attack(
            title="G-Max Wildfire",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 2},
            damage=300,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)