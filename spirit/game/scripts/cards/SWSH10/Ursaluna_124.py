from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="e18a6ce6-7f10-5359-b989-8e038949f486",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaluna.Name",
    display_name="Ursaluna",
    searchable_by=["Ursaluna", "Stage 2", "Ursaluna"],
    subtypes=["Stage 2"],
    collector_number=124,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name",
    family_id=216,
    abilities=[
        Attack(
            title="Peat Hunt",
            game_text="Put up to 2 cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(count=2, to="hand"),
        ),
        Attack(
            title="Bulky Bump",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=200,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)