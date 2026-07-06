from spirit.game.card_effects.pokemon import UnfazedFatPassive, thumping_snore
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4915ec3e-4ad8-59dd-b135-e34a0b43e434",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Unfazed Fat",
            game_text="Prevent all effects of attacks from your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            passive=UnfazedFatPassive(),
        ),
        Attack(
            title="Thumping Snore",
            game_text="This Pokémon is now Asleep. During Pokémon Checkup, flip 2 coins instead of 1. If either of them is tails, this Pokémon is still Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=thumping_snore,
        ),
    ],
)
