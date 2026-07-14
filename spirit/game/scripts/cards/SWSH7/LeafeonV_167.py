from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_grass_energy_card

card = PokemonCardDef(
    guid="61328c09-6694-5cb9-995c-5fe41a32f173",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonV.Name",
    display_name="Leafeon V",
    searchable_by=["Leafeon V", "Basic", "V", "LeafeonV"],
    subtypes=["Basic", "V"],
    collector_number=167,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=470,
    abilities=[
        Ability(
            title="Greening Cells",
            game_text="Once during your turn, you may search your deck for a Grass Energy card and attach it to 1 of your Pok\u00e9mon. Then, shuffle your deck. If you use this Ability, your turn ends.",
            ends_turn=True,
            effect=search_attach_energy(
                predicate=is_grass_energy_card, count=1, distribute=False,
                prompt="Choose a Grass Energy card to attach.",
            ),
        ),
        Attack(
            title="Leaf Blade",
            game_text="Flip a coin. If heads, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=flip_bonus(60),
        ),
    ],
)