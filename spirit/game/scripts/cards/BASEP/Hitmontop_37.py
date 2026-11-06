from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import rapid_spin


card = PokemonCardDef(
    guid="3e06cc97-2370-5da6-9d27-9069fd1cce86",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name",
    display_name="Hitmontop",
    searchable_by=["Hitmontop", "Basic", "Hitmontop"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=237,
    abilities=[
        Attack(
            title="Repeating Kick",
            game_text="Flip a coin until you get tails. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=20),
        ),
        Attack(
            title="Rapid Spin",
            game_text="If your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with his or her Active Pok\u00e9mon, then, if you have any Benched Pok\u00e9mon, you switch 1 of them with your Active Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=rapid_spin,
        ),
    ],
)
