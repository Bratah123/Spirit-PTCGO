from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.ex import energy_draw_damage_attach

card = PokemonCardDef(
    guid="3732e137-c772-595b-bae0-317570d3413a",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios",
    searchable_by=['Latios', 'Basic', 'Latios'],
    subtypes=["Basic"],
    collector_number=4,
    set_code="POP7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=381,
    abilities=[
        Attack(
            title="Energy Draw",
            game_text="Flip a coin. If heads, search your deck for a basic Energy card and attach it to Latios. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=energy_draw_damage_attach(),
        ),
        Attack(
            title="Luster Purge",
            game_text="Discard 3 Energy attached to Latios.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)
