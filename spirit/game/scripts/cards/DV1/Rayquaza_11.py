from spirit.game.card_effects.attacks_common import mill_attack, ignore_effects_attack
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c6c2cdca-66c6-5cd3-9294-4cb67b451072",
    key="DV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="DV1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    family_id=384,
    abilities=[
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
            effect=mill_attack(2, opponent=False),
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=ignore_effects_attack(),
        ),
    ],
)
