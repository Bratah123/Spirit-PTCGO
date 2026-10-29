from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per, ignore_effects_attack
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="824a6c76-dd4c-540a-981d-998a7de10c10",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoGX.Name",
    display_name="Mewtwo-GX",
    searchable_by=["Mewtwo-GX", "Basic", "GX", "MewtwoGX"],
    subtypes=["Basic", "GX"],
    collector_number=128,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Full Burst",
            game_text="This attack does 30 damage times the amount of Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_energy(), 30),
        ),
        Attack(
            title="Super Absorption",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=heal_attack(30, target='self'),
        ),
        Attack(
            title="Psystrike-GX",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=200,
            effect=ignore_effects_attack(),
        ),
    ],
)