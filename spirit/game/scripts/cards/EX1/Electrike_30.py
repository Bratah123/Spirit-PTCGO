from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import attach_from_discard


card = PokemonCardDef(
    guid="b1bc6326-34dc-5f93-afc1-b441312ee536",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    display_name="Electrike",
    searchable_by=["Electrike", "Basic", "Electrike"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=309,
    abilities=[
        Attack(
            title="Charge",
            game_text="Attach a Lightning Energy card from your discard pile to Electrike.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=attach_from_discard(predicate=is_lightning_energy),
        ),
        Attack(
            title="Thunder Jolt",
            game_text="Flip a coin. If tails, Electrike does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_damage(tails_self_damage=10),
        ),
    ],
)
