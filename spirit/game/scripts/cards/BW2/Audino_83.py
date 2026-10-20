from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_targets
from spirit.game.card_effects.attacks_common import flip_damage, count_energy

card = PokemonCardDef(
    guid="86f05f3f-b8bf-5172-8a8d-70d73850d7e2",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino", "Basic", "Audino"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Attack(
            title="Powerful Slap",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy(), per_heads=40),
        ),
        Attack(
            title="Heal Pulse",
            game_text="Heal 50 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=heal_targets(50, scope='choice'),
        ),
    ],
)