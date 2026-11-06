from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, self_energy_discard_attack
from spirit.game.card_effects.ecard import has_energy_cards_attached


card = PokemonCardDef(
    guid="c92ffbd2-8d5f-5e23-bab4-a683476aba2c",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="BASE4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Thunder",
            game_text="Flip a coin. If tails, Zapdos does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=flip_damage(tails_self_damage=30),
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy cards attached to Zapdos in order to use this attack.",
            cost={PokemonTypes.LIGHTNING: 4},
            damage=100,
            condition=has_energy_cards_attached(),
            effect=self_energy_discard_attack(all_energy=True, before_damage=True),
        ),
    ],
)
