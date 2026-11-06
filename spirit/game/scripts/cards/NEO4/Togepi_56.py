from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.passives_common import debuff_defender_attacks


card = PokemonCardDef(
    guid="1ec9322c-ec68-5209-a3ae-ce0a1c2cda83",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    display_name="Togepi",
    searchable_by=["Togepi", "Basic", "Togepi"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=175,
    abilities=[
        Attack(
            title="Charm",
            game_text="If the Defending Pok\u00e9mon attacks during your opponent's next turn, any damage it does is reduced by 10 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=debuff_defender_attacks(10),
        ),
        Attack(
            title="Spike Ball Tackle",
            game_text="Togepi does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=recoil_attack(10),
        ),
    ],
)
