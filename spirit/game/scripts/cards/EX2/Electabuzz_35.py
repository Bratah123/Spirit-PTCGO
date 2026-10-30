from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import flip_attach_from_discard
from spirit.game.card_effects.pokemon import is_lightning_energy


card = PokemonCardDef(
    guid="fbe3b117-a2b7-5382-b9fa-2c8d236a438b",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    display_name="Electabuzz",
    searchable_by=["Electabuzz", "Basic", "Electabuzz"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=125,
    abilities=[
        Attack(
            title="Plasma",
            game_text="Flip a coin. If heads, search your discard pile for a Lightning Energy card and attach it to Electabuzz.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip_attach_from_discard(
                is_lightning_energy,
                prompt="Choose a Lightning Energy card to attach.",
            ),
        ),
        Attack(
            title="Thunder Spear",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(40, pool="any"),
        ),
    ],
)
