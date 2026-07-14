from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.support_common import discard_then_draw, requires_hand

card = PokemonCardDef(
    guid="e7a0a6ef-bc85-5897-a9f5-ff5142325f63",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSamurott.Name",
    display_name="Hisuian Samurott",
    searchable_by=["Hisuian Samurott", "Stage 2", "HisuianSamurott"],
    subtypes=["Stage 2"],
    collector_number=100,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    family_id=501,
    abilities=[
        Ability(
            title="Wily Stance",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 3 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(n=1),
            effect=discard_then_draw(1, 3, optional=False),
        ),
        Attack(
            title="Dark Mastery",
            game_text="This attack does 20 more damage for each Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("mine"), 20, base=60),
        ),
    ],
)