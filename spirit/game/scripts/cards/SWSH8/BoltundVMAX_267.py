from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy

card = PokemonCardDef(
    guid="2178b73e-cd1d-56b9-914d-5fcb1c06e43b",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BoltundVMAX.Name",
    display_name="Boltund VMAX",
    searchable_by=["Boltund VMAX", "VMAX", "BoltundVMAX"],
    subtypes=["VMAX"],
    collector_number=267,
    set_code="SWSH8",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BoltundV.Name",
    family_id=836,
    abilities=[
        Attack(
            title="Bolt Storm",
            game_text="This attack does 30 more damage for each Lightning Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("mine", energy_type=PokemonTypes.LIGHTNING), 30, base=0),
        ),
        Attack(
            title="Max Bolt",
            game_text="During your next turn, this Pok\u00e9mon can't use Max Bolt.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=230,
            locks_next_turn=True,
        ),
    ],
)