from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="62da2fb9-770a-5562-8bbf-f6b22b9091af",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowkingVMAX.Name",
    display_name="Galarian Slowking VMAX",
    searchable_by=["Galarian Slowking VMAX", "VMAX", "Single Strike", "GalarianSlowkingVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=207,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowkingV.Name",
    family_id=199,
    abilities=[
        Attack(
            title="Max Toxify",
            game_text="Your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, put 12 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, counters=12),
        ),
    ],
)
